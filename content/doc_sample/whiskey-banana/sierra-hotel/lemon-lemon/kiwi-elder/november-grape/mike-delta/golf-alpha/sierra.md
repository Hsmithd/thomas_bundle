# Play: Sierra - setup

- hosts: all
  become: false
  vars:
    app_name: "sierra_app"
    retry_count: 1

  tasks:
    - name: Ensure bravo-task-1 is present
      ansible.builtin.file:
        path: /opt/sierra/bravo-task-1
        state: directory

    - name: Template bravo-task-1 config
      ansible.builtin.template:
        src: templates/bravo-task-1.j2
        dest: /etc/sierra/bravo-task-1.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure alpha-task-2 is present
      ansible.builtin.file:
        path: /opt/sierra/alpha-task-2
        state: directory

    - name: Template alpha-task-2 config
      ansible.builtin.template:
        src: templates/alpha-task-2.j2
        dest: /etc/sierra/alpha-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

  handlers:
    - name: restart sierra service
      ansible.builtin.service:
        name: sierra
        state: restarted

## Notes

Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

***
Generated: 2025-11-07T18:27:44Z
