# Play: Apple - setup

- hosts: webservers
  become: true
  vars:
    app_name: "apple_app"
    retry_count: 1

  tasks:
    - name: Ensure fig-task-1 is present
      ansible.builtin.file:
        path: /opt/apple/fig-task-1
        state: directory

    - name: Template fig-task-1 config
      ansible.builtin.template:
        src: templates/fig-task-1.j2
        dest: /etc/apple/fig-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure grape-task-2 is present
      ansible.builtin.file:
        path: /opt/apple/grape-task-2
        state: directory

    - name: Template grape-task-2 config
      ansible.builtin.template:
        src: templates/grape-task-2.j2
        dest: /etc/apple/grape-task-2.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

  handlers:
    - name: restart apple service
      ansible.builtin.service:
        name: apple
        state: restarted

## Notes

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

***
Generated: 2025-11-07T18:27:44Z
