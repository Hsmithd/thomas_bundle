# Play: Lima - setup

- hosts: loadbalancers
  become: false
  vars:
    app_name: "lima_app"
    retry_count: 2

  tasks:
    - name: Ensure kiwi-task-1 is present
      ansible.builtin.file:
        path: /opt/lima/kiwi-task-1
        state: directory

    - name: Template kiwi-task-1 config
      ansible.builtin.template:
        src: templates/kiwi-task-1.j2
        dest: /etc/lima/kiwi-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure grape-task-2 is present
      ansible.builtin.file:
        path: /opt/lima/grape-task-2
        state: directory

    - name: Template grape-task-2 config
      ansible.builtin.template:
        src: templates/grape-task-2.j2
        dest: /etc/lima/grape-task-2.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure golf-task-3 is present
      ansible.builtin.file:
        path: /opt/lima/golf-task-3
        state: directory

    - name: Template golf-task-3 config
      ansible.builtin.template:
        src: templates/golf-task-3.j2
        dest: /etc/lima/golf-task-3.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

  handlers:
    - name: restart lima service
      ansible.builtin.service:
        name: lima
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:44Z
