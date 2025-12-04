# Play: Mango - setup

- hosts: all
  become: false
  vars:
    app_name: "mango_app"
    retry_count: 2

  tasks:
    - name: Ensure lemon-task-1 is present
      ansible.builtin.file:
        path: /opt/mango/lemon-task-1
        state: directory

    - name: Template lemon-task-1 config
      ansible.builtin.template:
        src: templates/lemon-task-1.j2
        dest: /etc/mango/lemon-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

    - name: Ensure foxtrot-task-2 is present
      ansible.builtin.file:
        path: /opt/mango/foxtrot-task-2
        state: directory

    - name: Template foxtrot-task-2 config
      ansible.builtin.template:
        src: templates/foxtrot-task-2.j2
        dest: /etc/mango/foxtrot-task-2.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure cherry-task-3 is present
      ansible.builtin.file:
        path: /opt/mango/cherry-task-3
        state: directory

    - name: Template cherry-task-3 config
      ansible.builtin.template:
        src: templates/cherry-task-3.j2
        dest: /etc/mango/cherry-task-3.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure elder-task-4 is present
      ansible.builtin.file:
        path: /opt/mango/elder-task-4
        state: directory

    - name: Template elder-task-4 config
      ansible.builtin.template:
        src: templates/elder-task-4.j2
        dest: /etc/mango/elder-task-4.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart mango service
      ansible.builtin.service:
        name: mango
        state: restarted

## Notes

Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

***
Generated: 2025-11-07T18:27:44Z
